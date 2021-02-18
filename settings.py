
logging_config = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'std_format': {
            'format': '{asctime}-{module}-{levelname}-{message}',
            'style': '{'
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'log.log',
            'level': 'DEBUG',
            'formatter': 'std_format'
        }
    },
    'loggers': {
        'combination_logger': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': False
        }
    }
}