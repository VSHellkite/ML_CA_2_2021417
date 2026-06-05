from youtube_comment_downloader import YoutubeCommentDownloader
import csv

dl = YoutubeCommentDownloader()
comments = dl.get_comments_from_url("https://www.youtube.com/watch?v=m1fq9jxKZ68")

with open("comments.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["created_at", "title", "platform", "text"])
    w.writeheader()
    for c in comments:
        w.writerow({
            "created_at": c.get("time", ""),
            "title": c.get("author", ""),
            "platform": "YouTube",
            "text": c.get("text", ""),
        })
 