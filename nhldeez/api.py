from requests import get, Response
from urllib.parse import urljoin

BASEURL = "https://statsapi.web.nhl.com/"


def build_url(*args) -> str:
    return urljoin(BASEURL, "/".join(["api", "v1", *args]))


def conferences(id: int = None) -> Response:
    return get(build_url("conferences", "" if id is None else str(id)))


def divisions(id: int = None) -> Response:
    return get(build_url("divisions", "" if id is None else str(id)))


def draft(year: int = None) -> Response:
    return get(build_url("draft", "" if year is None else str(year)))


def draft_prospects(id: int = None) -> Response:
    return get(build_url("draft/prospects", "" if id is None else str(id)))


def game_boxscore(game_id: int) -> Response:
    return get(build_url("game", str(game_id), "boxscore"))


def game_content(game_id: int) -> Response:
    return get(build_url("game", str(game_id), "content"))


def game_feed(game_id: int) -> Response:
    return get(build_url("game", str(game_id), "feed", "live"))


def get_schedule(season: int, team_id: int = None, game_type: str = None) -> Response:
    return get(
        build_url("schedule"),
        params={
            "season": f"{season}{season+1}",
            "teamId": team_id,
            "gameType": game_type,
        },
    )
