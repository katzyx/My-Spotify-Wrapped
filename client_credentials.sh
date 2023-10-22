
# client_id = "84b6f9b3a8b345ac9497f330d9f3a52f"
# client_secret = "5af34ce6cb8e42e5900b7bc3166b8607"
curl -X POST "https://accounts.spotify.com/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id=84b6f9b3a8b345ac9497f330d9f3a52f&client_secret=5af34ce6cb8e42e5900b7bc3166b8607"
