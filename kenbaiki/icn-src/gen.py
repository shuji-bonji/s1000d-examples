base='''<!doctype html><meta charset="utf-8"><style>
*{box-sizing:border-box}html,body{margin:0}
body{width:800px;height:480px;font-family:"Noto Sans CJK JP","Noto Sans JP","IPAGothic",sans-serif;background:#eef2f6;color:#10233a;display:flex;flex-direction:column}
.top{height:56px;background:#12406b;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 24px;font-size:20px}
.mid{flex:1;padding:20px 28px;display:flex;flex-direction:column;gap:14px}
.bot{height:64px;background:#dbe3ec;display:flex;align-items:center;gap:16px;padding:0 24px}
.btn{border:2px solid #12406b;border-radius:10px;background:#fff;font-size:22px;padding:14px 22px;text-align:center}
.pri{background:#1f6fb5;color:#fff;border-color:#1f6fb5}
.sub{font-size:18px;padding:8px 20px;border-radius:8px;border:2px solid #5b6b7d;background:#fff}
h1{font-size:24px;margin:0}.row{display:flex;gap:14px}.row .btn{flex:1}
.box{background:#fff;border:1px solid #b8c4d1;border-radius:8px;padding:12px 16px;font-size:20px}
.warn{background:#fff3cd;border-color:#d39e00}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.grid .btn{font-size:19px;padding:10px}.sel{background:#ffe9a8}
</style>'''
def page(title,mid,bot):
    return base+f'<div class="top"><span>{title}</span><span>10:25　出発駅：みなと中央</span></div><div class="mid">{mid}</div><div class="bot">{bot}</div>'
P={
'00001':page('指定席券売機','<h1>ご利用の内容を選んでください</h1><div class="btn pri">乗換案内から購入</div><div class="row"><div class="btn">払い戻し</div><div class="btn">定期券の更新</div></div>','<div class="sub">取り消し</div><div class="sub">前の画面</div>'),
'00002':page('到着駅の選択','<div class="row"><div class="box" style="flex:1">出発駅：みなと中央</div><div class="sub" style="align-self:center">変更する</div></div><h1>到着駅を選んでください</h1><div class="grid"><div class="btn">さくら台</div><div class="btn sel">北みどり</div><div class="btn">東川原</div><div class="btn">山の手口</div><div class="btn">新港</div><div class="btn">西ヶ丘</div><div class="btn">南ふ頭</div><div class="btn">空港前</div></div>','<div class="sub">取り消し</div><div style="flex:1"></div><div class="btn pri" style="padding:8px 40px">次へ</div>'),
'00003':page('お支払い','<h1>IC カードをかざしてください</h1><div class="box">みなと中央 → 北みどり　指定席 1 枚</div><div class="box" style="font-size:28px;text-align:right">お支払い金額　2,480 円</div><div class="box" style="text-align:center;border-style:dashed">IC カードの読み取り部にカードをかざす</div>','<div class="sub">取り消し</div><div class="sub">前の画面</div>'),
'00004':page('残高不足','<div class="box warn"><b>残高が不足しています</b></div><div class="box">お支払い金額　2,480 円<br>カードの残高　1,200 円</div><div class="row"><div class="btn pri">チャージする</div><div class="btn">別の支払い方法</div></div>','<div class="sub">戻る</div>'),
}
for k,v in P.items(): open(f's{k}.html','w').write(v)
open('s00005.html','w').write('''<!doctype html><meta charset="utf-8"><body style="margin:0"><svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480" font-family="Noto Sans CJK JP,sans-serif" font-size="20">
<rect width="800" height="480" fill="#fff"/>
<rect x="230" y="20" width="300" height="440" fill="#d9dee4" stroke="#333" stroke-width="2"/>
<rect x="245" y="110" width="270" height="335" fill="#6f95c9" stroke="#333" stroke-width="2"/>
<rect x="265" y="40" width="230" height="60" fill="#1e2b3a" stroke="#333"/>
<rect x="478" y="240" width="18" height="80" rx="4" fill="#e89b1c" stroke="#333" stroke-width="2"/>
<circle cx="487" cy="215" r="9" fill="#fff" stroke="#333" stroke-width="2"/><line x1="487" y1="210" x2="487" y2="220" stroke="#333" stroke-width="2"/>
<g stroke="#333" stroke-width="1.5" fill="none"><line x1="496" y1="280" x2="600" y2="280"/><line x1="496" y1="215" x2="600" y2="180"/><line x1="380" y1="300" x2="150" y2="300"/></g>
<g fill="#111"><circle cx="620" cy="280" r="16" fill="#fff" stroke="#333"/><text x="614" y="287">1</text><text x="645" y="287">取っ手</text>
<circle cx="620" cy="176" r="16" fill="#fff" stroke="#333"/><text x="614" y="183">2</text><text x="645" y="183">鍵穴</text>
<circle cx="130" cy="300" r="16" fill="#fff" stroke="#333"/><text x="124" y="307">3</text><text x="40" y="340">前面扉</text></g>
</svg>''')
