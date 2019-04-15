import os, subprocess

class FileAnalysis():
    name = "File Analysis"
    info = "Generates basic metadata listings for files"
    options = {
        'FILEPATH':"",
        'HASH':'sha512',
        'FILETYPE':True,
        'STAT':True,
    }

    def __hash(self, filepath, algorithm):
        algorithms = ['md5','sha256', 'sha512']
        if algorithm in algorithms:
            algorithm += "sum"
        output = subprocess.run([algorithm,
                                 filepath],stdout=subprocess.PIPE).stdout.decode('utf-8').split()[0]
        return output

    def __filetype(self, filepath):
        command = ['file', filepath]
        output = subprocess.run(command,stdout=subprocess.PIPE).stdout.decode('utf-8').split()
        del(output[0])
        return output

    def __stat(self, filepath):
        command = ['stat', filepath]
        output = subprocess.run(command,stdout=subprocess.PIPE).stdout.decode('utf-8')
        return output


    def run(self):
        output = ""
        options = self.options
        filepath = options['FILEPATH']
        if not os.path.exists(filepath):
            print("File at path {0} does not exit".format(filepath))
            return None
        filehash = self.__hash(filepath, options['HASH'])
        output += "{0} hash: {1}\n\n".format(options['HASH'],filehash)
        if options['FILETYPE']:
            filetype = self.__filetype(filepath)
            output += "File Type: {0}\n\n".format(filetype)
        if options['STAT']:
            stat = self.__stat(filepath)
            output += "Stat: {0}\n".format(stat)
        return output

