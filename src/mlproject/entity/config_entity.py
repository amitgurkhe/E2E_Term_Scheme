from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)  # no need of self, useful in defining data_type
class DataingestionConfig:
  root_dir: Path
  source_url: str
  local_data_file: Path
  unzip_dir : Path 