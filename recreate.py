#!/usr/bin/env python3
from datetime import datetime


def most_recent_release_at_date(pkg_repo_url: str,
                                date: datetime
                                ) -> str:
    """
    Determines the most recent tagged release of a given project that was
    available at a given date and time.

    Args:
        pkg_repo_url: The URL of the Git repository used to host the source
            code for the package.
        date: The date that should be used when determining the most recent
            tagged release.

    Returns:
        The name of the release that was available at that moment in time.

    Raises:
        Exception: if no release was available at the given date.
            (TODO: add custom exception.)
    """
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
