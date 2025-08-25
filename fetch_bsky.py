#!/usr/bin/env python3
import os, json, requests, datetime
from dotenv import load_dotenv

load_dotenv()
HANDLE   = os.getenv("BSKY_HANDLE")
PASSWORD = os.getenv("BSKY_APP_PASSWORD")

session = requests.post(
    "https://bsky.social/xrpc/com.atproto.server.createSession",
    json={"identifier": HANDLE, "password": PASSWORD}
).json()
token   = session["accessJwt"]

feed = requests.get(
    f"https://bsky.social/xrpc/app.bsky.feed.getAuthorFeed?actor={HANDLE}&limit=5",
    headers={"Authorization": f"Bearer {token}"}
).json()["feed"]

posts = [
    {
        "id": item["post"]["uri"].split("/")[-1],
        "text": item["post"]["record"]["text"][:120] + "…",
        "created_at": item["post"]["record"]["createdAt"]
    }
    for item in feed
]

os.makedirs("data", exist_ok=True)
with open("data/bluesky.json", "w") as f:
    json.dump({"bluesky": posts, "handle": HANDLE}, f)