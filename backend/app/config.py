from decouple import config


class Settings:
    # Calendly Configuration
    CALENDLY_TOKEN = config('CALENDLY_TOKEN', default='')
    CALENDLY_SLUG = config('CALENDLY_SLUG', default='')

    # API Configuration
    API_HOST = config('API_HOST', default='0.0.0.0')
    API_PORT = config('API_PORT', default=8000, cast=int)
    DEBUG = config('DEBUG', default=True, cast=bool)


settings = Settings()