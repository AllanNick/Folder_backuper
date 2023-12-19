# Folder_backuper
 automatically back files on your system

# Useage:
 availiable options in current software:
 "freq", which is the frequency of backup action, using 's' as unit
 "screen_buffer", which is the handle of log output on your terminal
 "src" , which is the source/target folder/file you are going to backup

 Eg:
 backuping 'test_folder' every '30s' and 'output' log on terminal:

    PS[Important!]: src folder should use absolute path
    [software design and debugging hasn't take good considerate of processing realtive path due to limited time]

        [{
            "mode" : "realtive",
            "src": "D:\\Programs\\python_projects\\autobkp\\test_src",
            "dst": "",
            "freq": "30",
            "log_level": "INFO",
            "screen_buffer" : "ON"
        }]

 about OTHER options in 'conf.json':
 plz !DO NOT! modifi if you don't know what you are doing

