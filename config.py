"""Typeless AIディクテーション完全ガイド - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "Typeless AIディクテーション完全ガイド"
BLOG_DESCRIPTION = "AI音声ディクテーションTypelessの使い方・最新機能・料金を毎日更新。100言語対応・キーボード不要の新しい文章作成術を完全解説。"
BLOG_URL = "https://musclelove-777.github.io/typeless-guide"
BLOG_TAGLINE = "タイピング卒業宣言 — Typelessで声だけで書く時代へ"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "MuscleLove-777/typeless-guide"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "Typeless 使い方",
    "Typeless 料金・プラン",
    "Typeless vs Wispr Flow",
    "Typeless 最新ニュース",
    "AI音声ディクテーション",
    "Typeless 活用テクニック",
    "音声入力ツール比較",
    "Typeless 多言語対応",
]

THEME = {
    "primary": "#7C3AED",
    "accent": "#EC4899",
    "gradient_start": "#7C3AED",
    "gradient_end": "#EC4899",
    "dark_bg": "#0a0a1a",
    "dark_surface": "#1a1030",
    "light_bg": "#faf5ff",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 2
SCHEDULE_HOURS = [8, 18]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "Typeless Pro": [
        {"service": "Typeless Pro", "url": "https://typeless.ch", "description": "Typeless Proに登録する"},
    ],
    "AI音声入力": [
        {"service": "Typeless", "url": "https://typeless.ch", "description": "Typelessを無料で始める"},
    ],
    "音声入力デバイス": [
        {"service": "Amazon マイク", "url": "https://www.amazon.co.jp", "description": "Amazonで高品質マイクを探す"},
    ],
    "オンライン講座": [
        {"service": "Udemy", "url": "https://www.udemy.com", "description": "UdemyでAI活用講座を探す"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "AmazonでAI関連書籍を探す"},
        {"service": "楽天ブックス", "url": "https://www.rakuten.co.jp", "description": "楽天でAI関連書籍を探す"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)
DASHBOARD_PORT = 8092
