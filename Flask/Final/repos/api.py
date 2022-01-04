from .exceptions import GitHubApiException
from .models import GitHubRepo
import requests

api_url = "https://api.github.com/search/repositories"

def create_query(languages, min_star=50000) -> str:
    query = f"stars:>{min_star} "

    languages_query_list = [f"langugage:{lang.strip()}" for lang in languages]
    languages_query = " ".join(languages_query_list)

    return query + languages_query

def repos_with_most_stars(languages, sort="stars", order="desc") -> list:
    params = {
        "q": create_query(languages),
        "sort": sort,
        "order": order
    }

    response = requests.get(api_url, params=params)
    status_code = response.status_code

    if status_code != 200:
        raise GitHubApiException(status_code)
    else:
        response_json = response.json()

        return [GitHubRepo(item["name"], item["language"], item["stargazers_count"]) for item in response_json["items"]]
