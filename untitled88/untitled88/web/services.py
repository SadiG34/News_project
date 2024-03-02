def filter_news(news_qs, filters: dict):
    if filters.__contains__('search'):
        news_qs = news_qs.filter(title__icontains=filters['search']) \
                  | news_qs.filter(text__icontains=filters['search'])

    return news_qs


def filter_comment(comments, news):
    comments = comments.filter(news=news)
    return comments