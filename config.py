class Config:
    def __init__(self, filename):
        # Fallback settings
        prefix = "."
        status = "meow meow"
        nickname = ""
        use_nickname = False
        warnings = True
        use_status = False
        setting_names: list[str] = ["prefix", "use_status", "status", "warnings", "use_nickname", "nickname"]
        config_file = open("config", 'r')
        for line in config_file.readlines():
            if line.startswith(";"):
                continue
            else:
                for name in setting_names:
                    if line.startswith(name + "=", 0, len(name) + 1):
                       if isinstance(locals()[name], str):
                            helper: str = line
                            helper = helper[(len(name) + 2):]
                            if(name == "prefix"):
                                self.prefix = helper
                            if(name == "status"):
                                self.status = helper
                            if(name == "nickname"):
                                self.nickname = helper
                       elif isinstance(locals()[name], bool):
                            helper: str = line
                            helper2: bool = False
                            helper = helper[(len(name) + 2):]
                            if helper.__contains__("true"):
                                helper2 = True
                            if(name == "use_status"):
                                self.use_status = helper2
                            if(name == "use_nickname"):
                                self.use_nickname = helper2
                            if(name == "warnings"):
                                self.warnings = helper

        print(self.prefix, self.use_status, self.status, self.warnings, self.use_nickname, self.nickname)
