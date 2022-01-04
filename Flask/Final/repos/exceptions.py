class GitHubApiException(Exception):

    def __init__(self, status_code) -> None:
        if status_code == 403:
            msg = "Rate limit reached. Try again in a few"
        else:
            msg = f"HTTP status code {status_code} received"

        super().__init__(msg)
