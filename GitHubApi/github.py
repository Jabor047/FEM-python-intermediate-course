import requests
# from pprint import pprint as pp

def repos_with_most_stars(api_url, languages, sort="stars", order="desc") -> dict:

    params = {
        "q": create_query(languages),
        "sort": sort,
        "order": order
    }

    response = requests.get(api_url, params=params)
    status_code = response.status_code

    if status_code == 403:
        raise RuntimeError("Rate limit reached. Please wait a minute and try again.")
    if status_code == 200:
        raise RuntimeError(f"An error occured. HTTP status code was: {status_code}")
    else:
        response_json = response.json()

        # pp(response_json)

        return(response_json["items"])

def create_query(languages, min_star=50000) -> str:
    query = f"stars:>{min_star} "

    for language in languages:
        query += f"language:{language} "

    return query

if __name__ == "__main__":
    try:
        api_url = "https://api.github.com/search/repositories"

        results = repos_with_most_stars(api_url, ["python", "javascript", "ruby"])

        for result in results:
            language = result["language"]
            stars = result["stargazers_count"]
            name = result["name"]

            print(f"-> {name} is a {language} repo.It has {stars} stars")
    except RuntimeError as e:
        print(f"something wrong happened: {e}")
