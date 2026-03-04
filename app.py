import streamlit as st
import google.generativeai as genai
import random

# 1. إعدادات الصفحة والهوية البصرية
st.set_page_config(page_title="Q-Fazaa | كيو فزعة", page_icon="🎓", layout="centered")

# CSS متقدم لتحسين الواجهة ودعم الـ Dark Mode
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
    html, body, [class*="css"] { 
        font-family: 'Tajawal', sans-serif; 
        text-align: right; 
        direction: rtl; 
    }
    
    .main-header { 
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        color: white; padding: 30px; border-radius: 20px; text-align: center; 
        margin-bottom: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    .joke-box { 
        background-color: #fff9db; color: #856404; padding: 20px; 
        border-radius: 15px; text-align: center; margin-bottom: 25px; 
        font-weight: bold; border: 2px dashed #fcc419; font-size: 18px;
    }
    
    .option-card {
        background-color: white; padding: 20px; border-radius: 15px;
        border-right: 8px solid #1a73e8; box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 20px; color: #333;
    }
    
    .stButton>button { 
        background: linear-gradient(45deg, #1a73e8, #0d47a1); color: white;
        height: 3em; border-radius: 12px; font-size: 18px !important; 
        transition: 0.3s; border: none; font-weight: bold;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 5px 15px rgba(26,115,232,0.4); }

    /* دعم الدارك مود */
    @media (prefers-color-scheme: dark) {
        .option-card {
            background-color: #1a1a1a !important;
            color: #f8f9fa !important;
            border-right: 8px solid #4dadff !important;
        }
        .joke-box {
            background-color: #2b2b2b !important;
            color: #ffd43b !important;
            border-color: #fab005 !important;
        }
        h1, h2, h3, h4, p, span, label { color: white !important; }
        .main-header p { color: #f8f9fa !important; }
    }
    </style>
    """, unsafe_allow_html=True)

# 2. نظام المفاتيح المتعدد (Load Balancing)
try:
    keys = [st.secrets.get("GOOGLE_API_KEY"), st.secrets.get("KEY2"), st.secrets.get("KEY3")]
    active_keys = [k for k in keys if k]
    selected_key = random.choice(active_keys)
    genai.configure(api_key=selected_key)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except:
    st.error("⚠️ تأكدي من إعداد الـ API Key في الـ Secrets")
    st.stop()

# 3. الهيدر (الشعار الجديد)
st.markdown('<div class="main-header"><h1>🎓 كيو فزعة | Q-Fazaa</h1><p>فزعتك بجيبك.. وإيميلك يخلص موضوعك ⚡</p></div>', unsafe_allow_html=True)

# 4. الأهداف والذبات
target = st.selectbox("🎯 وش هدفك من الإيميل؟", 
                     ["طلب بونص درجات", "تحويل المحاضرة أونلاين", "تأخر عن محاضرة", "غيبت عن محاضرة", "تنزيل مادة أو فتح شعبة", "تغيير شعبة"])

jokes = {
    "طلب بونص درجات": ["تكفى يا دكتور.. بمسك عيالك بس عطني هالعشر درجات هههههه", "الدرجات وسخ دنيا يا دكتور، طهرني منها وعطني بونص!"],
    "تحويل المحاضرة أونلاين": ["طريق المليداء اليوم يبي له سباحة مو سيارة.. خلوها عن بعد!", "السرير ينادينا يا دكتور، والجو براد.. أونلاين أزين"],
    "تأخر عن محاضرة": ["باص الجامعة قرر يسوي جولة سياحية بالقصيم قبل يجينا", "زحمة المليداء خلتني أراجع قرارات حياتي وأنا بالسيارة"],
    "غيبت عن محاضرة": ["السكليف جاهز.. بس الأخلاق تبي بونص غياب", "المنبه خانني يا دكتور، والثقة انعدمت بيننا"],
    "تنزيل مادة أو فتح شعبة": ["نفاذ معلق.. وبوابة الجامعة تذكرني بأيام الحصن", "كل الشعب قفلت.. صرت أحس إني بمسلسل صراع العروش"],
    "تغيير شعبة": ["الوقت بعز القايلة يا دكتور.. والمخيخ يفصل عندي هههههه", "عندي تعارض يخلي راسي يدور.. الفزعة نبي ننقل!"]
}

st.markdown(f'<div class="joke-box">💡 {random.choice(jokes[target])}</div>', unsafe_allow_html=True)

# 5. منطقة الأعذار التفاعلية
st.markdown('<div class="option-card">', unsafe_allow_html=True)
st.write("🔍 **حدد تفاصيل عذرك:**")
reason = ""
col1, col2 = st.columns(2)

if target == "طلب بونص درجات":
    with col1: hard = st.checkbox("الاختبار كان تعجيزي")
    with col2: group = st.checkbox("طلب جماعي من الشعبة")
    reason = f"صعوبة: {hard}, جماعي: {group}"
elif target == "تحويل المحاضرة أونلاين":
    with col1: exams = st.checkbox("ضغط اختبارات ثانية")
    with col2: weather = st.checkbox("ظروف الجو اليوم")
    reason = f"اختبارات: {exams}, جو: {weather}"
elif target == "تأخر عن محاضرة":
    with col1: bus = st.checkbox("الباص تأخر")
    with col2: traffic = st.checkbox("زحمة الطريق")
    reason = f"باص: {bus}, زحمة: {traffic}"
elif target == "غيبت عن محاضرة":
    with col1: sick = st.checkbox("عندي سكليف")
    with col2: family = st.checkbox("ظرف عائلي")
    reason = f"مرض: {sick}, عائلي: {family}"
elif target == "تنزيل مادة أو فتح شعبة":
    with col1: nafaz = st.checkbox("نفاذ معلق")
    with col2: grad = st.checkbox("خريج/ة")
    reason = f"نفاذ: {nafaz}, تخرج: {grad}"
elif target == "تغيير شعبة":
    with col1: conflict = st.checkbox("تعارض مواد")
    with col2: qaila = st.checkbox("وقت القايلة (حر)")
    reason = f"تعارض: {conflict}, قايلة: {qaila}"

st.markdown('</div>', unsafe_allow_html=True)

mood = st.select_slider("🎭 أسلوب الدكتور/ة:", options=["رسمي جداً", "نظامي", "حبيب/ة"], value="نظامي")

# 6. التشغيل والتوليد
if st.button("🚀 ولّد الإيميل الفزعة"):
    with st.spinner('جاري حبك الأعذار...'):
        try:
            prompt = f"اكتب إيميل لـ {target}. الأعذار: {reason}. المزاج: {mood}. مختصر جداً."
            res = model.generate_content(prompt)
            st.session_state['initial'] = res.text
        except: st.error("السيرفر مضغوط، جرب ثانية")

if 'initial' in st.session_state:
    st.markdown("---")
    st.info(st.session_state['initial'])
    if st.button("✨ حوله لأسلوب واقعي (بلمسة قصيمية)"):
        with st.spinner('جاري إضافة الملح والبهارات...'):
            try:
                real_p = f"حول هذا لواقعي لبق بلهجة بيضاء قصيمية خفيفة جداً: {st.session_state['initial']}"
                res_real = model.generate_content(real_p)
                st.session_state['real'] = res_real.text
            except: st.error("خطأ في التوليد")

if 'real' in st.session_state:
    st.success(st.session_state['real'])
    st.balloons()

st.markdown(f'<div style="text-align:center; color:#888; margin-top:50px;">تطوير المهندسة حنين 1/2 | GDG Qassim 🚀</div>', unsafe_allow_html=True)