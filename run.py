from app import create_app
from flask import request, jsonify, render_template
from youtube_transcript_api import YouTubeTranscriptApi

app = create_app()

# The `/summarize` routes are implemented inside the `main` blueprint
# (see `app/main.py`). Removed duplicate handlers here to avoid
# route conflicts and ensure `url_for('main.summarize')` resolves.


if __name__ == "__main__":
    try:
        app.run(debug=True, use_reloader=False)
    except Exception as e:
        print(f"Error starting Flask app: {e}")
        import traceback
        traceback.print_exc()