import os
import logging
from from_root import from_root
from datetime import datetime

log_file = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
#log_file = f"log_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
log_path = os.path.join(from_root() , "log",log_file)
os.mkdirs(log_path,exist_ok = True)
log_file_path = os.path.join(log_path)

logging.basicConfig(
    filename= log_file_path,
    format = '[%(asctime)s] %(lineno)d %(name)s %(levelname)s %(message)s',
    level = logging.info
    
)


