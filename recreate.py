#!/usr/bin/env python3

def recreate_historical_rosinstall(repo_url: str,
                                   commit_sha: str
                                   ) -> str:
    """
    Produces a ROS install that estimates the state of a given project and its
    dependencies at a specific moment in time, corresponding to a given commit.


    Args:
        repo_url: The URL of the Git repository for the project that one wishes
            to recreate.
        commit_sha: The SHA of the commit that corresponds to the version of the
            Git repository that one wishes to recreate.

    Returns:
        A string containing the rosinstall file.
    """
    raise NotImplementedError
