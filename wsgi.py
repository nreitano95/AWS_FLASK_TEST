from app import app

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8542))
    app.run(port=port, debug=True) 

