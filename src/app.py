from flask import Flask, jsonify
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hi():
    return "hi"

@app.route("/coupon")
def coupon():
    data = {
        'text':
        '''
        [아라] 안녕하세요. 아라를 방문해 주셔서 감사드립니다.

 

고객님의
* #{새해 감사 상품 10% 추가 할인 쿠폰} *
사용 기간이 곧 만료됩니다

 

[쿠폰 사용 안내]: 
쿠폰명:
#{새해 감사 상품 10% 추가 할인 쿠폰} 
사용 종료일: #{1월 25일 2020년}
#{상품 바로가기 https://ara.travelflan.com/products/1249}

 

* 쿠폰 사용 종료 기간은 #{4월 30일}까지이며 유효기간이 지나면 사용 여부와 관계없이 자동 소멸 됩니다.

 

항상 좋은 혜택으로 보답 하겠습니다.
감사드립니다.
        ''',
        'hello': 'hi',
        'title': 'coupon'
    }

    return jsonify(data)

@app.route("/event")
def event():
    data = {
        'text':
        '''
        하이 이것은 이벤트 입니다.
        #ㅁㄴㅇㄹㅁㄴㅇㄹ
        ''',
        'hello': 'bye',
        'title': 'event'
    }

    return jsonify(data)

@app.route('/post', methods=['POST'])
def post():
    return "good"

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')