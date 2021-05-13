import utils
import os.path as op
import os
from zipfile import ZipFile


class BaseArchive:
    def __init__(self, source_path, destination_path):
        self.source_path = source_path
        self.destination_path = destination_path

    def file_archive(self, filename):
        raise NotImplementedError

    def folder_archive(self, filename):
        raise NotImplementedError

    def extract(self, filename):
        raise NotImplementedError

    def extract_all(self):
        raise NotImplementedError


class Zip(BaseArchive):
    def __init__(self, source_path, destination_path):
        super().__init__(source_path, destination_path)

    def file_archive(self, filename):  # Source path is a file
        zipobj = ZipFile(self.destination_path + f'/{filename}.zip', 'w')
        zipobj.write(self.source_path, op.basename(self.source_path))
        zipobj.close()
        print("Process has completed Successfully")

    def folder_archive(self, filename):  # Source path is a directory | Destination path  directory(to create a zip)
        zipobj = ZipFile(self.destination_path + f'/{filename}.zip', 'w')
        for file in os.listdir(self.source_path):
            zipobj.write(self.source_path + f'/{file}', file)
        zipobj.close()
        print("Process has completed Successfully")

    def extract(self, filename):  # Source path is a zip
        zipobj = ZipFile(self.source_path, 'r')
        zipobj.extract(filename, self.destination_path)
        zipobj.close()
        print("Process has completed Successfully")

    def extract_all(self):  # Source path is a zip
        zipobj = ZipFile(self.source_path, 'r')
        zipobj.extractall(self.destination_path)
        zipobj.close()
        print("Process has completed Successfully")

#  Class RAR(BaseArchive)
#  Class TAR(BaseArchive)
# ....


ArchiveList = [".zip", ".rar", ".tar", ".gz"]
SourcePath = utils.path_input_validation("Source Path")
# 1) directory(extension='')   2)archive file  3)other file


if SourcePath[1] is None:  # Source path is a directory | Destination path must be a directory | Archive name required
    DestinationPath = utils.path_input_validation("Destination path:", "d")
    ArchiveName = input("Archive name: \n>> ")
    ArchiveFormat = utils.input_validation("Archive format?(.zip , .rar, ...) ", *ArchiveList)

    if ArchiveFormat == '.zip':
        ArchiveObject = Zip(SourcePath[0], DestinationPath[0])
        ArchiveObject.folder_archive(ArchiveName)

    # if ArchiveFormat == '.rar'
    # if ArchiveFormat == '.gz'
    # ...

elif SourcePath[1] in ArchiveList:  # Source path is an archive file | Despath directory | Action required
    DestinationPath = utils.path_input_validation("Destination path:", "d")
    ActionType = utils.input_validation("Extract All or Specific file [A/S]?", 'A', 'S')
    if SourcePath[1] == '.zip':
        ArchiveObject = Zip(SourcePath[0], DestinationPath[0])
        if ActionType == 'A':
            ArchiveObject.extract_all()
        else:
            TempZip = ZipFile(SourcePath[0])
            FileName = utils.input_validation("File name:", *TempZip.namelist())
            TempZip.close()
            ArchiveObject.extract(FileName)

    # if ArchiveFormat == '.rar'
    # if ArchiveFormat == '.gz'
    # ...

else:  # Source path is a file | Destination path directory | Archive name required
    DestinationPath = utils.path_input_validation("Destination path", "d")
    ArchiveName = input("Archive name: \n>> ")
    ArchiveFormat = utils.input_validation("Archive format?(.zip , .rar, ...) ", *ArchiveList)

    if ArchiveFormat == ".zip":
        ArchiveObject = Zip(SourcePath[0], DestinationPath[0])
        ArchiveObject.file_archive(ArchiveName)

    # if ArchiveFormat == '.rar'
    # if ArchiveFormat == '.gz'
    # ...

