import lambda_function

import config

pr_id = 2324
pr_author = 'balloob'
base_branch = 'release/78'
head_branch = 'feature/fix-X'

github_event = """
{
  "action": "opened",
  "number": {pr_id},
  "pull_request": {
    "url": "https://api.github.com/repos/{repo_owner}/{repo}/pulls/1",
    "id": 34778301,
    "html_url": "https://github.com/{repo_owner}/{repo}/pull/1",
    "diff_url": "https://github.com/{repo_owner}/{repo}/pull/1.diff",
    "patch_url": "https://github.com/{repo_owner}/{repo}/pull/1.patch",
    "issue_url": "https://api.github.com/repos/{repo_owner}/{repo}/issues/1",
    "number": 2315,
    "state": "open",
    "locked": false,
    "title": "Update the README with new information",
    "user": {
      "login": "{pr_author}",
      "id": 6752317,
      "avatar_url": "https://avatars.githubusercontent.com/u/6752317?v=3",
      "gravatar_id": "",
      "url": "https://api.github.com/users/{pr_author}",
      "html_url": "https://github.com/{pr_author}",
      "followers_url": "https://api.github.com/users/{pr_author}/followers",
      "following_url": "https://api.github.com/users/{pr_author}/following{/other_user}",
      "gists_url": "https://api.github.com/users/{pr_author}/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/{pr_author}/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/{pr_author}/subscriptions",
      "organizations_url": "https://api.github.com/users/{pr_author}/orgs",
      "repos_url": "https://api.github.com/users/{pr_author}/repos",
      "events_url": "https://api.github.com/users/{pr_author}/events{/privacy}",
      "received_events_url": "https://api.github.com/users/{pr_author}/received_events",
      "type": "User",
      "site_admin": false
    },
    "body": "This is a pretty simple change that we need to pull into master.",
    "created_at": "2015-05-05T23:40:27Z",
    "updated_at": "2015-05-05T23:40:27Z",
    "closed_at": null,
    "merged_at": null,
    "merge_commit_sha": null,
    "assignee": null,
    "milestone": null,
    "commits_url": "https://api.github.com/repos/{repo_owner}/{repo}/pulls/1/commits",
    "review_comments_url": "https://api.github.com/repos/{repo_owner}/{repo}/pulls/1/comments",
    "review_comment_url": "https://api.github.com/repos/{repo_owner}/{repo}/pulls/comments{/number}",
    "comments_url": "https://api.github.com/repos/{repo_owner}/{repo}/issues/1/comments",
    "statuses_url": "https://api.github.com/repos/{repo_owner}/{repo}/statuses/0d1a26e67d8f5eaf1f6ba5c57fc3c7d91ac0fd1c",
    "head": {
      "label": "{pr_author}:{head_branch}",
      "ref": "{head_branch}",
      "sha": "0d1a26e67d8f5eaf1f6ba5c57fc3c7d91ac0fd1c",
      "user": {
        "login": "{pr_author}",
        "id": 6752317,
        "avatar_url": "https://avatars.githubusercontent.com/u/6752317?v=3",
        "gravatar_id": "",
        "url": "https://api.github.com/users/{pr_author}",
        "html_url": "https://github.com/{pr_author}",
        "followers_url": "https://api.github.com/users/{pr_author}/followers",
        "following_url": "https://api.github.com/users/{pr_author}/following{/other_user}",
        "gists_url": "https://api.github.com/users/{pr_author}/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/{pr_author}/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/{pr_author}/subscriptions",
        "organizations_url": "https://api.github.com/users/{pr_author}/orgs",
        "repos_url": "https://api.github.com/users/{pr_author}/repos",
        "events_url": "https://api.github.com/users/{pr_author}/events{/privacy}",
        "received_events_url": "https://api.github.com/users/{pr_author}/received_events",
        "type": "User",
        "site_admin": false
      },
      "repo": {
        "id": 35129377,
        "name": "{repo}",
        "full_name": "{repo_owner}/{repo}",
        "owner": {
          "login": "{repo_owner}",
          "id": 6752317,
          "avatar_url": "https://avatars.githubusercontent.com/u/6752317?v=3",
          "gravatar_id": "",
          "url": "https://api.github.com/users/{repo_owner}",
          "html_url": "https://github.com/{repo_owner}",
          "followers_url": "https://api.github.com/users/{repo_owner}/followers",
          "following_url": "https://api.github.com/users/{repo_owner}/following{/other_user}",
          "gists_url": "https://api.github.com/users/{repo_owner}/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/{repo_owner}/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/{repo_owner}/subscriptions",
          "organizations_url": "https://api.github.com/users/{repo_owner}/orgs",
          "repos_url": "https://api.github.com/users/{repo_owner}/repos",
          "events_url": "https://api.github.com/users/{repo_owner}/events{/privacy}",
          "received_events_url": "https://api.github.com/users/{repo_owner}/received_events",
          "type": "User",
          "site_admin": false
        },
        "private": false,
        "html_url": "https://github.com/{repo_owner}/{repo}",
        "description": "",
        "fork": false,
        "url": "https://api.github.com/repos/{repo_owner}/{repo}",
        "forks_url": "https://api.github.com/repos/{repo_owner}/{repo}/forks",
        "keys_url": "https://api.github.com/repos/{repo_owner}/{repo}/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/{repo_owner}/{repo}/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/{repo_owner}/{repo}/teams",
        "hooks_url": "https://api.github.com/repos/{repo_owner}/{repo}/hooks",
        "issue_events_url": "https://api.github.com/repos/{repo_owner}/{repo}/issues/events{/number}",
        "events_url": "https://api.github.com/repos/{repo_owner}/{repo}/events",
        "assignees_url": "https://api.github.com/repos/{repo_owner}/{repo}/assignees{/user}",
        "branches_url": "https://api.github.com/repos/{repo_owner}/{repo}/branches{/branch}",
        "tags_url": "https://api.github.com/repos/{repo_owner}/{repo}/tags",
        "blobs_url": "https://api.github.com/repos/{repo_owner}/{repo}/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/{repo_owner}/{repo}/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/{repo_owner}/{repo}/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/{repo_owner}/{repo}/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/{repo_owner}/{repo}/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/{repo_owner}/{repo}/languages",
        "stargazers_url": "https://api.github.com/repos/{repo_owner}/{repo}/stargazers",
        "contributors_url": "https://api.github.com/repos/{repo_owner}/{repo}/contributors",
        "subscribers_url": "https://api.github.com/repos/{repo_owner}/{repo}/subscribers",
        "subscription_url": "https://api.github.com/repos/{repo_owner}/{repo}/subscription",
        "commits_url": "https://api.github.com/repos/{repo_owner}/{repo}/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/{repo_owner}/{repo}/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/{repo_owner}/{repo}/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/{repo_owner}/{repo}/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/{repo_owner}/{repo}/contents/{+path}",
        "compare_url": "https://api.github.com/repos/{repo_owner}/{repo}/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/{repo_owner}/{repo}/merges",
        "archive_url": "https://api.github.com/repos/{repo_owner}/{repo}/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/{repo_owner}/{repo}/downloads",
        "issues_url": "https://api.github.com/repos/{repo_owner}/{repo}/issues{/number}",
        "pulls_url": "https://api.github.com/repos/{repo_owner}/{repo}/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/{repo_owner}/{repo}/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/{repo_owner}/{repo}/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/{repo_owner}/{repo}/labels{/name}",
        "releases_url": "https://api.github.com/repos/{repo_owner}/{repo}/releases{/id}",
        "created_at": "2015-05-05T23:40:12Z",
        "updated_at": "2015-05-05T23:40:12Z",
        "pushed_at": "2015-05-05T23:40:26Z",
        "git_url": "git://github.com/{repo_owner}/{repo}.git",
        "ssh_url": "git@github.com:{repo_owner}/{repo}.git",
        "clone_url": "https://github.com/{repo_owner}/{repo}.git",
        "svn_url": "https://github.com/{repo_owner}/{repo}",
        "homepage": null,
        "size": 0,
        "stargazers_count": 0,
        "watchers_count": 0,
        "language": null,
        "has_issues": true,
        "has_downloads": true,
        "has_wiki": true,
        "has_pages": true,
        "forks_count": 0,
        "mirror_url": null,
        "open_issues_count": 1,
        "forks": 0,
        "open_issues": 1,
        "watchers": 0,
        "default_branch": "{base_branch}"
      }
    },
    "base": {
      "label": "{repo_owner}:{base_branch}",
      "ref": "{base_branch}",
      "sha": "9049f1265b7d61be4a8904a9a27120d2064dab3b",
      "user": {
        "login": "{repo_owner}",
        "id": 6752317,
        "avatar_url": "https://avatars.githubusercontent.com/u/6752317?v=3",
        "gravatar_id": "",
        "url": "https://api.github.com/users/{repo_owner}",
        "html_url": "https://github.com/{repo_owner}",
        "followers_url": "https://api.github.com/users/{repo_owner}/followers",
        "following_url": "https://api.github.com/users/{repo_owner}/following{/other_user}",
        "gists_url": "https://api.github.com/users/{repo_owner}/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/{repo_owner}/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/{repo_owner}/subscriptions",
        "organizations_url": "https://api.github.com/users/{repo_owner}/orgs",
        "repos_url": "https://api.github.com/users/{repo_owner}/repos",
        "events_url": "https://api.github.com/users/{repo_owner}/events{/privacy}",
        "received_events_url": "https://api.github.com/users/{repo_owner}/received_events",
        "type": "User",
        "site_admin": false
      },
      "repo": {
        "id": 35129377,
        "name": "{repo}",
        "full_name": "{repo_owner}/{repo}",
        "owner": {
          "login": "{repo_owner}",
          "id": 6752317,
          "avatar_url": "https://avatars.githubusercontent.com/u/6752317?v=3",
          "gravatar_id": "",
          "url": "https://api.github.com/users/{repo_owner}",
          "html_url": "https://github.com/{repo_owner}",
          "followers_url": "https://api.github.com/users/{repo_owner}/followers",
          "following_url": "https://api.github.com/users/{repo_owner}/following{/other_user}",
          "gists_url": "https://api.github.com/users/{repo_owner}/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/{repo_owner}/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/{repo_owner}/subscriptions",
          "organizations_url": "https://api.github.com/users/{repo_owner}/orgs",
          "repos_url": "https://api.github.com/users/{repo_owner}/repos",
          "events_url": "https://api.github.com/users/{repo_owner}/events{/privacy}",
          "received_events_url": "https://api.github.com/users/{repo_owner}/received_events",
          "type": "User",
          "site_admin": false
        },
        "private": false,
        "html_url": "https://github.com/{repo_owner}/{repo}",
        "description": "",
        "fork": false,
        "url": "https://api.github.com/repos/{repo_owner}/{repo}",
        "forks_url": "https://api.github.com/repos/{repo_owner}/{repo}/forks",
        "keys_url": "https://api.github.com/repos/{repo_owner}/{repo}/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/{repo_owner}/{repo}/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/{repo_owner}/{repo}/teams",
        "hooks_url": "https://api.github.com/repos/{repo_owner}/{repo}/hooks",
        "issue_events_url": "https://api.github.com/repos/{repo_owner}/{repo}/issues/events{/number}",
        "events_url": "https://api.github.com/repos/{repo_owner}/{repo}/events",
        "assignees_url": "https://api.github.com/repos/{repo_owner}/{repo}/assignees{/user}",
        "branches_url": "https://api.github.com/repos/{repo_owner}/{repo}/branches{/branch}",
        "tags_url": "https://api.github.com/repos/{repo_owner}/{repo}/tags",
        "blobs_url": "https://api.github.com/repos/{repo_owner}/{repo}/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/{repo_owner}/{repo}/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/{repo_owner}/{repo}/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/{repo_owner}/{repo}/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/{repo_owner}/{repo}/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/{repo_owner}/{repo}/languages",
        "stargazers_url": "https://api.github.com/repos/{repo_owner}/{repo}/stargazers",
        "contributors_url": "https://api.github.com/repos/{repo_owner}/{repo}/contributors",
        "subscribers_url": "https://api.github.com/repos/{repo_owner}/{repo}/subscribers",
        "subscription_url": "https://api.github.com/repos/{repo_owner}/{repo}/subscription",
        "commits_url": "https://api.github.com/repos/{repo_owner}/{repo}/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/{repo_owner}/{repo}/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/{repo_owner}/{repo}/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/{repo_owner}/{repo}/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/{repo_owner}/{repo}/contents/{+path}",
        "compare_url": "https://api.github.com/repos/{repo_owner}/{repo}/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/{repo_owner}/{repo}/merges",
        "archive_url": "https://api.github.com/repos/{repo_owner}/{repo}/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/{repo_owner}/{repo}/downloads",
        "issues_url": "https://api.github.com/repos/{repo_owner}/{repo}/issues{/number}",
        "pulls_url": "https://api.github.com/repos/{repo_owner}/{repo}/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/{repo_owner}/{repo}/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/{repo_owner}/{repo}/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/{repo_owner}/{repo}/labels{/name}",
        "releases_url": "https://api.github.com/repos/{repo_owner}/{repo}/releases{/id}",
        "created_at": "2015-05-05T23:40:12Z",
        "updated_at": "2015-05-05T23:40:12Z",
        "pushed_at": "2015-05-05T23:40:26Z",
        "git_url": "git://github.com/{repo_owner}/{repo}.git",
        "ssh_url": "git@github.com:{repo_owner}/{repo}.git",
        "clone_url": "https://github.com/{repo_owner}/{repo}.git",
        "svn_url": "https://github.com/{repo_owner}/{repo}",
        "homepage": null,
        "size": 0,
        "stargazers_count": 0,
        "watchers_count": 0,
        "language": null,
        "has_issues": true,
        "has_downloads": true,
        "has_wiki": true,
        "has_pages": true,
        "forks_count": 0,
        "mirror_url": null,
        "open_issues_count": 1,
        "forks": 0,
        "open_issues": 1,
        "watchers": 0,
        "default_branch": "{base_branch}"
      }
    },
    "_links": {
      "self": {
        "href": "https://api.github.com/repos/{repo_owner}/{repo}/pulls/1"
      },
      "html": {
        "href": "https://github.com/{repo_owner}/{repo}/pull/1"
      },
      "issue": {
        "href": "https://api.github.com/repos/{repo_owner}/{repo}/issues/1"
      },
      "comments": {
        "href": "https://api.github.com/repos/{repo_owner}/{repo}/issues/1/comments"
      },
      "review_comments": {
        "href": "https://api.github.com/repos/{repo_owner}/{repo}/pulls/1/comments"
      },
      "review_comment": {
        "href": "https://api.github.com/repos/{repo_owner}/{repo}/pulls/comments{/number}"
      },
      "commits": {
        "href": "https://api.github.com/repos/{repo_owner}/{repo}/pulls/1/commits"
      },
      "statuses": {
        "href": "https://api.github.com/repos/{repo_owner}/{repo}/statuses/0d1a26e67d8f5eaf1f6ba5c57fc3c7d91ac0fd1c"
      }
    },
    "merged": false,
    "mergeable": null,
    "mergeable_state": "unknown",
    "merged_by": null,
    "comments": 0,
    "review_comments": 0,
    "commits": 1,
    "additions": 1,
    "deletions": 1,
    "changed_files": 1
  },
  "repository": {
    "id": 35129377,
    "name": "{repo}",
    "full_name": "{repo_owner}/{repo}",
    "owner": {
      "login": "{repo_owner}",
      "id": 6752317,
      "avatar_url": "https://avatars.githubusercontent.com/u/6752317?v=3",
      "gravatar_id": "",
      "url": "https://api.github.com/users/{repo_owner}",
      "html_url": "https://github.com/{repo_owner}",
      "followers_url": "https://api.github.com/users/{repo_owner}/followers",
      "following_url": "https://api.github.com/users/{repo_owner}/following{/other_user}",
      "gists_url": "https://api.github.com/users/{repo_owner}/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/{repo_owner}/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/{repo_owner}/subscriptions",
      "organizations_url": "https://api.github.com/users/{repo_owner}/orgs",
      "repos_url": "https://api.github.com/users/{repo_owner}/repos",
      "events_url": "https://api.github.com/users/{repo_owner}/events{/privacy}",
      "received_events_url": "https://api.github.com/users/{repo_owner}/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/{repo_owner}/{repo}",
    "description": "",
    "fork": false,
    "url": "https://api.github.com/repos/{repo_owner}/{repo}",
    "forks_url": "https://api.github.com/repos/{repo_owner}/{repo}/forks",
    "keys_url": "https://api.github.com/repos/{repo_owner}/{repo}/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/{repo_owner}/{repo}/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/{repo_owner}/{repo}/teams",
    "hooks_url": "https://api.github.com/repos/{repo_owner}/{repo}/hooks",
    "issue_events_url": "https://api.github.com/repos/{repo_owner}/{repo}/issues/events{/number}",
    "events_url": "https://api.github.com/repos/{repo_owner}/{repo}/events",
    "assignees_url": "https://api.github.com/repos/{repo_owner}/{repo}/assignees{/user}",
    "branches_url": "https://api.github.com/repos/{repo_owner}/{repo}/branches{/branch}",
    "tags_url": "https://api.github.com/repos/{repo_owner}/{repo}/tags",
    "blobs_url": "https://api.github.com/repos/{repo_owner}/{repo}/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/{repo_owner}/{repo}/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/{repo_owner}/{repo}/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/{repo_owner}/{repo}/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/{repo_owner}/{repo}/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/{repo_owner}/{repo}/languages",
    "stargazers_url": "https://api.github.com/repos/{repo_owner}/{repo}/stargazers",
    "contributors_url": "https://api.github.com/repos/{repo_owner}/{repo}/contributors",
    "subscribers_url": "https://api.github.com/repos/{repo_owner}/{repo}/subscribers",
    "subscription_url": "https://api.github.com/repos/{repo_owner}/{repo}/subscription",
    "commits_url": "https://api.github.com/repos/{repo_owner}/{repo}/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/{repo_owner}/{repo}/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/{repo_owner}/{repo}/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/{repo_owner}/{repo}/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/{repo_owner}/{repo}/contents/{+path}",
    "compare_url": "https://api.github.com/repos/{repo_owner}/{repo}/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/{repo_owner}/{repo}/merges",
    "archive_url": "https://api.github.com/repos/{repo_owner}/{repo}/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/{repo_owner}/{repo}/downloads",
    "issues_url": "https://api.github.com/repos/{repo_owner}/{repo}/issues{/number}",
    "pulls_url": "https://api.github.com/repos/{repo_owner}/{repo}/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/{repo_owner}/{repo}/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/{repo_owner}/{repo}/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/{repo_owner}/{repo}/labels{/name}",
    "releases_url": "https://api.github.com/repos/{repo_owner}/{repo}/releases{/id}",
    "created_at": "2015-05-05T23:40:12Z",
    "updated_at": "2015-05-05T23:40:12Z",
    "pushed_at": "2015-05-05T23:40:26Z",
    "git_url": "git://github.com/{repo_owner}/{repo}.git",
    "ssh_url": "git@github.com:{repo_owner}/{repo}.git",
    "clone_url": "https://github.com/{repo_owner}/{repo}.git",
    "svn_url": "https://github.com/{repo_owner}/{repo}",
    "homepage": null,
    "size": 0,
    "stargazers_count": 0,
    "watchers_count": 0,
    "language": null,
    "has_issues": true,
    "has_downloads": true,
    "has_wiki": true,
    "has_pages": true,
    "forks_count": 0,
    "mirror_url": null,
    "open_issues_count": 1,
    "forks": 0,
    "open_issues": 1,
    "watchers": 0,
    "default_branch": "master"
  },
  "sender": {
    "login": "{pr_author}",
    "id": 6752317,
    "avatar_url": "https://avatars.githubusercontent.com/u/6752317?v=3",
    "gravatar_id": "",
    "url": "https://api.github.com/users/{pr_author}",
    "html_url": "https://github.com/{pr_author}",
    "followers_url": "https://api.github.com/users/{pr_author}/followers",
    "following_url": "https://api.github.com/users/{pr_author}/following{/other_user}",
    "gists_url": "https://api.github.com/users/{pr_author}/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/{pr_author}/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/{pr_author}/subscriptions",
    "organizations_url": "https://api.github.com/users/{pr_author}/orgs",
    "repos_url": "https://api.github.com/users/{pr_author}/repos",
    "events_url": "https://api.github.com/users/{pr_author}/events{/privacy}",
    "received_events_url": "https://api.github.com/users/{pr_author}/received_events",
    "type": "User",
    "site_admin": false
  }
}
"""

for search, replace in {
  'pr_id': str(pr_id),
  'pr_author': pr_author,
  'repo_owner': config.repo_owner,
  'repo': config.repo,
  'base_branch': base_branch,
  'head_branch': head_branch,
}.items():
    github_event = github_event.replace('{' + search + '}', replace)

sns_wrapper = {
    'Records': [{
        'Sns': {
            'Message': github_event,
            'MessageAttributes': {
                'X-Github-Event': {
                    'Value': 'pull_request'
                }
            }
        }
    }]
}

lambda_function.lambda_handler(sns_wrapper, None, debug=True)
