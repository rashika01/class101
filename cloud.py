import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A2OixFJeOHT9gR8Yc8ZwR4WIugMoGyqvJcsa5qJQTYyKx-DrcgFAGdsVH10_vL5dE6p52cgVtWZgYxWz-zsvCwyxd1rjKRkR86w-aYyd4cUZ5UPx5QUzgMGKsOUwQUqBpWk2pio'
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer")
    file_to = input("enter the full path to upload to dropbox")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been uploaded")


main()