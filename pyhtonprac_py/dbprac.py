from pymongo import MongoClient
client = MongoClient('')
db = client.dbsparta

# url은 mongoDB Cloud 홈페이지에서 Database connect 탭에서 발급받아 사용한다
# url 'mongodb+srv://ID:PASSWORD@cluster0.38yzx.mongodb.net/CLUSTERNAME?retryWrites=true&w=majority'
# dbsparta는 db이름 users는 컬렉션으로 사용할 이름

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
all_users = list(db.users.find({}, {'_id': False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})

# 역정렬해서 첫번째 아이디 뽑아내기
print(list(db.guest_book.find({},{'_id':False}).sort('id',-1))[0]['id'])