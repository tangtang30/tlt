import argparse


def preload(parser: argparse.ArgumentParser):
    parser.add_argument(
        "--cloudflared",
        action="store_true",
        help="use trycloudflare, alternative to gradio --share",
    )
    
    parser.add_argument(
        "--tunnel-webhook", type=str, help="discord webhook to send tunnel url to"
    )
