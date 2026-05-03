import os
import json
import sys
class FileUtility:
 def __init__(self, directory):
  self.directory = directory
 def list_files(self):
  return os.listdir(self.directory)
 def read_file(self, filename):
  with open(os.path.join(self.directory, filename), 'r') as file:
   return file.read()
 def write_file(self, filename, content):
  with open(os.path.join(self.directory, filename), 'w') as file:
   file.write(content)
 def delete_file(self, filename):
  os.remove(os.path.join(self.directory, filename))
 def file_exists(self, filename):
  return os.path.isfile(os.path.join(self.directory, filename))
 def create_directory(self, name):
  os.makedirs(os.path.join(self.directory, name), exist_ok=True)
 def delete_directory(self, name):
  os.rmdir(os.path.join(self.directory, name))
 def get_file_size(self, filename):
  return os.path.getsize(os.path.join(self.directory, filename))
 def to_json(self, data, filename):
  with open(os.path.join(self.directory, filename), 'w') as file:
   json.dump(data, file)
 def from_json(self, filename):
  with open(os.path.join(self.directory, filename), 'r') as file:
   return json.load(file)
 def copy_file(self, src, dst):
  import shutil
  shutil.copy(os.path.join(self.directory, src), os.path.join(self.directory, dst))
 def move_file(self, src, dst):
  import shutil
  shutil.move(os.path.join(self.directory, src), os.path.join(self.directory, dst))
