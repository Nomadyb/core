from django.apps import AppConfig

#import profiles.signals  
"""
eğer profiles.signals doğrudan import edilirse hazır olmadığı için doğrudan (signals yüklenmeden önce apps yüklenir bu sebeple çökme olabilir.)
apps üzerinden kullanacaığı için program çökebilir.Bu sebeple ready methodu ile yapılmalıdır.
"""

class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    def ready(self):
        import profiles.signals