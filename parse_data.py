import os

class Parser:
    def __init__(self, config_file_path, work_experience_file_path, edu_file_path, languages_file_path):
        self.data_info = {}
        self.data_work_experience = {}
        self.data_edu = {}
        self.data_lang = {}
        self.config_file_path = config_file_path
        self.work_experience_file_path = work_experience_file_path
        self.edu_file_path = edu_file_path
        self.languages_file_path = languages_file_path

    def get_data(self):
        return self.data_info
    
    def get_data_work(self):
        return self.data_work_experience

    def get_data_edu(self):
        return self.data_edu

    def get_data_lang(self):
        return self.data_lang

    def read_config_file(self):
        with open(self.config_file_path, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                self.data_info[key] = value

    def read_work_file(self):
        with open(self.work_experience_file_path, 'r') as file:
            entry = {}
            entry_num = 1

            for line in file:
                key, value = line.strip().split('=')
                if key == "entry" and len(entry) != 0 or key == "end":
                    self.data_work_experience[entry_num] = entry
                    entry = {}
                    entry_num += 1
                if key != "entry":
                    entry[key] = value
   
    # Same functionality as reading work experience file, will change format later for this method
    def read_edu_file(self):
        with open(self.edu_file_path, 'r') as file:
            entry = {}
            entry_num = 1

            for line in file:
                key, value = line.strip().split('=')
                if key == "entry" and len(entry) != 0 or key == "end":
                    self.data_edu[entry_num] = entry
                    entry = {}
                    entry_num += 1
                if key != "entry":
                    entry[key] = value

    def read_lang_file(self):
        with open(self.languages_file_path, 'r') as file:
            entry = {}
            entry_num = 1

            for line in file:
                key, value = line.strip().split('=')
                if key == "entry" and len(entry) != 0 or key == "end":
                    self.data_lang[entry_num] = entry
                    entry = {}
                    entry_num += 1
                if key != "entry":
                    entry[key] = value


