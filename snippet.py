"""GitLab Snippets"""

import requests
from gitlab import config


class Snippet(object):
    """Snippets for GitLab"""

    @staticmethod
    def update_policies_snippet(content):
        """Update the nightly testing policies

        Args:
            content (str): Content for the snippet

        Returns:
            Response from GitLab API
        """
        return Snippet.update_snippet(config.POLICIES_ID, content)

    @staticmethod
    def update_snippet(snippet_id, content, **kwargs):
        """Update an existing snippet

        Args:
            snippet_id (str): ID string of the snippet
            content (str): Content for the snippet
            kwargs: Optional snippet arguments
                    title, file_name, visibility_level

        Returns:
            Response from GitLab API
        """
        data = {
            snippet_param: kwargs[snippet_param]
            for snippet_param in ('title', 'file_name', 'visibility_level')
            if snippet_param in kwargs
        }
        data.update({'content': content})
        headers = {'PRIVATE-TOKEN': config.SNIPPETS_TOKEN}
        update_url = '{}/{}'.format(config.GITLAB_URL, snippet_id)
        r = requests.put(
            update_url,
            headers=headers,
            data=data
        )
        return r.text
