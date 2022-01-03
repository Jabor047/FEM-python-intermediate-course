class GitHubApiError(Exception):

    def __init__(self, status_code) -> None:
        if status_code == 403:
            message = "Rate limit reached."
        else:
            message = f"Status code {status_code} received"

        super().__init__(message)
