@app.route('/myposts',methods=['GET','POST'])
def myposts():
    if request.method == 'POST':
        user = supabase_client.auth.get_session()
        user_id=user.user.id
        file = request.files['photo']
        photoname = file.filename

        bucket_name = 'bucket name'
        key = f'{user_id}/{photoname}'

        s3.upload_fileobj(file, bucket_name, key)
        
