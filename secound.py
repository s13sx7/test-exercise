from bs4 import BeautifulSoup
import requests
import json

# URL для получения твитов пользователя (исправленный URL)
url = 'https://api.x.com/graphql/E3opETHurmVJflFsUBVuUQ/UserTweets?variables=%7B%22userId%22%3A%2244196397%22%2C%22count%22%3A20%2C%22includePromotedContent%22%3Atrue%2C%22withQuickPromoteEligibilityTweetFields%22%3Atrue%2C%22withVoice%22%3Atrue%2C%22withV2Timeline%22%3Atrue%7D&features=%7B%22rweb_tipjar_consumption_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22communities_web_enable_tweet_community_results_fetch%22%3Atrue%2C%22c9s_tweet_anatomy_moderator_badge_enabled%22%3Atrue%2C%22articles_preview_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22creator_subscriptions_quote_tweet_preview_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22rweb_video_timestamps_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D&fieldToggles=%7B%22withArticlePlainText%22%3Afalse%7D'
# Ваш Bearer токен
bearer_token = "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"

# Заголовки для запроса
headers = {
    'Authorization': f'Bearer {bearer_token}',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 7_7_6) AppleWebKit/537.16 (KHTML, like Gecko) Chrome/48.0.2560.172 Safari/537',
    'Accept-Language': 'en-US,en;q=0.ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-Guest-Token': '1835159324571701681'
}

# Куки для запроса
cookies = {
    'night_mode': '2',
    'd_prefs': 'MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw',
    'dnt': '1',
    'guest_id': 'v1%3A171938068735478688',
    'guest_id_ads': 'v1%3A171938068735478688',
    'guest_id_marketing': 'v1%3A171938068735478688',
    'external_referer': 'padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|ziZgIoZIK4nlMKUVLq9KcnBFms0d9TqBqrE%2FyjvSFlFJR45yIlYF%2Bw%3D%3D',
    'gt': '1834602927027028255',
    'att': '1-LNmtOuvQMOtp2Yq9FnDKpSCQtofUjZnbSwSCA6V1',
    'personalization_id': 'v1_d7rvvqhpguRq9Z/6SgEevg==',
}

s = requests.Session()
s.headers.update(headers)
s.cookies.update(cookies)

response = s.get(url).json()
pars_response = response['data']['user']['result']['timeline_v2']['timeline']['instructions'][2]['entries']

with open('Elon_tweets.txt', 'w', encoding='utf-8') as f:
    for i in range(10):
        f.writelines(pars_response[i]['content']['itemContent']['tweet_results']['result']['legacy']['full_text']+'\n')