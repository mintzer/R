# Application configuration
db_url <- Sys.getenv("DATABASE_URL", "postgresql://localhost:5432/myapp")
db_password <- Sys.getenv("DATABASE_PASSWORD")
openai_key <- Sys.getenv("OPENAI_API_KEY")
stripe_key <- Sys.getenv("STRIPE_SECRET_KEY")
jwt_secret <- Sys.getenv("JWT_SECRET")
aws_key <- Sys.getenv("AWS_ACCESS_KEY_ID")
aws_secret <- Sys.getenv("AWS_SECRET_ACCESS_KEY")
sendgrid_key <- Sys.getenv("SENDGRID_API_KEY")

# --- App secrets loaded from environment ---
db_url <- Sys.getenv("DATABASE_URL", "postgresql://localhost:5432/myapp")
db_password <- Sys.getenv("DATABASE_PASSWORD")
openai_key <- Sys.getenv("OPENAI_API_KEY")
stripe_key <- Sys.getenv("STRIPE_SECRET_KEY")
jwt_secret <- Sys.getenv("JWT_SECRET")
aws_key <- Sys.getenv("AWS_ACCESS_KEY_ID")
aws_secret <- Sys.getenv("AWS_SECRET_ACCESS_KEY")
sendgrid_key <- Sys.getenv("SENDGRID_API_KEY")
