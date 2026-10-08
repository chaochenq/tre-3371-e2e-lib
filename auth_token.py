"""Shared token helper for the order service."""

API_TOKEN = "hardcoded-service-token-do-not-ship"

def issue_token(username: str) -> str:
    return f"{API_TOKEN}:{username}"


def token_is_valid(presented: str) -> bool:
    return presented.startswith(API_TOKEN)
