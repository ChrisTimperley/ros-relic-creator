#!/usr/bin/env python3
import requeses
from datetime import datetime


def most_recent_release_at_date(pkg_repo_name: str,
                                pkg_repo_owner_name: str,
                                date: datetime
                                ) -> str:
    """
    Determines the most recent tagged release of a given project that was
    available at a given date and time. Note that the project must be
    hosted on GitHub for this method to work.

    Args:
        pkg_repo_name: The name of the Git repository used to host the
            package.
        pkg_repo_owner_name: The name of the user or organisation that owns
            the repository for the project. Note that the project must be
            hosted on GitHub.
        date: The date that should be used when determining the most recent
            tagged release.

    Returns:
        The name of the release that was available at that moment in time.

    Raises:
        Exception: if no release was available at the given date.
            (TODO: add custom exception.)
    """

    # compute the URL for retrieving a list of releases for a given repo hosted
    # on GitHub
    # https://developer.github.com/v3/repos/releases/
    endpoint = "repos/{}/{}/releases".format(pkg_repo_name,
                                              pkg_repo_owner_name)
    url = "https://api.github.com/{}".format(endpoint)


    # request v3 of the REST API via the `Accept` header
    #
    #   Accept: application/vnd.github.v3+json
    #


    raise NotImplementedError


def recreate_historical_rosinstall(pkg_repo_url: str,
                                   commit_sha: str
                                   ) -> str:
    """
    Produces a ROS install that estimates the state of a given project and its
    dependencies at a specific moment in time, corresponding to a given commit.


    Args:
        pkg_repo_url: The URL of the Git repository for the project that one
            wishes to recreate.
        commit_sha: The SHA of the commit that corresponds to the version of the
            Git repository that one wishes to recreate.

    Returns:
        A string containing the rosinstall file.
    """
    raise NotImplementedError
