class GitHubRepo():
    def __init__(self, name, language, stars) -> None:
        self.name = name
        self.language = language
        self.stars = stars

    def __str__(self) -> str:
        return f"{self.name} is a {self.language} repo and has {self.stars} stars"

    def __repr__(self) -> str:
        return f"GitHubRepo({self.name, self.language, self.stars})"
