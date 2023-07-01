class Config:
    prefix: str = ""
    use_status: bool = False
    status: str = ""
    warnings: bool = False
    use_nickname: bool = False
    nickname: str = ""

    def get_config(file_name):
       """
       Load configs from a file
       Will initiate all the variables
       :return:
       """

       line_num: int = 0
       setting_names:list[str] = ["prefix", "use_status", "status", "warnings", "use_nickname", "nickname"]

       config_file = open("file", 'r')
       for line in config_file.readline():
          line_num += 1
          if line.startswith(";"):
             continue
          for name in setting_names:
            if line.startswith(name):
               if(isinstance(locals()[name]), str):
                  locals()[name] == line.replace(name, "")
                  locals[name] == str.rstrip(2)
               elif(isinstance(locals()[name], bool)):
                  TODO: "finish this shit later, im getting on hypixel"
