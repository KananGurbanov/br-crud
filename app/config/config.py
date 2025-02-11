import logging
import os
import yaml

from app.logger.logger import get_logger

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


def __parse_yaml():
    logger = get_logger(__name__)
    active_profile = os.environ.get('ACTIVE_PROFILE', default='local')
    path_to_yaml = f'application-{active_profile}.yaml'
    logger.info(f"ACTIVE PROFILE = {active_profile}")
    return yaml.safe_load(open(path_to_yaml))


config = __parse_yaml()
ACTIVE_PROFILE = os.environ.get('ACTIVE_PROFILE', default='local')