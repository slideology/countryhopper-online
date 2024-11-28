from ..app import app

# Vercel serverless function entry point
def handler(request, context):
    return app(request)
