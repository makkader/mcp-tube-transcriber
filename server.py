from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
from youtube_transcript_api import YouTubeTranscriptApi


# Initialize FastMCP server
mcp = FastMCP("tube-transcriber", version="0.1.0")


@mcp.tool()
def get_transcript(video_id: str) -> str:
    """
    Fetches the transcript for a given YouTube video ID.
    """
    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(video_id)
    total_transcript = ' '.join([snippet.text for snippet in fetched_transcript])
    return total_transcript

 