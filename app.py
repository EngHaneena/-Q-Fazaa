import streamlit as st
import google.generativeai as genai
import random

# 1. إعدادات الصفحة والهوية البصرية
st.set_page_config(page_title="Q-Fazaa | كيو فزعة", page_icon="🎓", layout="centered")

# CSS المتقدم
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; text-align: right; direction: rtl; }
    .main-header { background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%); color: white; padding: 30px; border-radius: 20px; text-align: center; margin-bottom: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
    .joke-box { background-color: #fff9db; color: #856404; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 25px; font-weight: bold; border: 2px dashed #fcc419; font-size: 18px; }
    .option-card { background-color: white; padding: 20px; border-radius: 15px; border-right: 8px solid #1a73e8; box-shadow: 0 2px 8px rgba(0,0,0,0.05); margin-bottom: 20px; color: #333; }
    .stButton>button { background: linear-gradient(45deg, #1a73e8, #0d47a1); color: white; height: 3em; border-radius: 12px; font-size: 18px !important; transition: 0.3s; border: none; font-weight: bold; width: 100%; }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 5px 15px rgba(26,115,232,0.4); }
    @media (prefers-color-scheme: dark) {
        .option-card { background-color: #1a1a1a !important; color: #f8f9fa !important; border-right: 8px solid #4dadff !important; }
        .joke-box { background-color: #2b2b2b !important; color: #ffd43b !important; border-color: #fab005 !important; }
        h1, h2, h3, h4, p, span, label { color: white !important; }
        .main-header p { color: #f8f9fa !important; }
    }
    </style>
    """, unsafe_allow_html=True)

# 2. إعداد الـ API
try:
    api_key = st.secrets.get("GOOGLE_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except:
    st.error("⚠️ تأكدي من إعداد الـ API Key في الـ Secrets")
    st.stop()

# 3. الهيدر
st.markdown('<div class="main-header"><h1>🎓 كيو فزعة | Q-Fazaa</h1><p>فزعتك بجيبك.. وإيميلك يخلص موضوعك ⚡</p></div>', unsafe_allow_html=True)

# 4. الأهداف 
target_options = [
    "طلب بونص درجات", 
    "تحويل المحاضرة أونلاين", 
    "تأخر عن محاضرة", 
    "غبت عن محاضرة", 
    "تنزيل مادة أو فتح شعبة", 
    "تغيير شعبة",
    "طلب إعفاء لغة إنجليزية"
]
target = st.selectbox("🎯 وش هدفك من الإيميل؟", target_options)

# قاموس الذبات (تمت إضافة ذبة زها)
jokes = {
    "طلب بونص درجات": ["تكفى يا دكتور.. بمسك عيالك بس عطني هالعشر درجات هههههه"],
    "تحويل المحاضرة أونلاين": ["طريق المليداء اليوم يبي له سباحة مو سيارة.. خلوها عن بعد!"],
    "تأخر عن محاضرة": ["باص الجامعة قرر يسوي جولة سياحية بالقصيم قبل يجينا"],
    "غبت عن محاضرة": ["السكليف جاهز.. بس الأخلاق تبي بونص غياب"],
    "تنزيل مادة أو فتح شعبة": ["نفاذ معلق.. وبوابة الجامعة تذكرني بأيام الحصن"],
    "تغيير شعبة": ["الوقت بعز القايلة يا دكتور.. والمخيخ يفصل عندي هههههه"],
    "طلب إعفاء لغة إنجليزية": ["بيحذفونه لك يا زها لا تخافين مانبي تهاويل! هههههههه"]
}

if target in jokes:
    st.markdown(f'<div class="joke-box">💡 {random.choice(jokes[target])}</div>', unsafe_allow_html=True)

# 5. منطقة التفاصيل
st.markdown('<div class="option-card">', unsafe_allow_html=True)
st.write("🔍 **حدد تفاصيل عذرك:**")
reason_details = ""
col1, col2 = st.columns(2)

if target == "طلب بونص درجات":
    with col1: hard = st.checkbox("الاختبار كان تعجيزي")
    with col2: group = st.checkbox("طلب جماعي")
    reason_details = f"صعوبة: {hard}, جماعي: {group}"
elif target == "تحويل المحاضرة أونلاين":
    with col1: exams = st.checkbox("ضغط اختبارات")
    with col2: weather = st.checkbox("ظروف الجو")
    reason_details = f"اختبارات: {exams}, جو: {weather}"
elif target == "تأخر عن محاضرة":
    with col1: bus = st.checkbox("الباص تأخر")
    with col2: traffic = st.checkbox("زحمة الطريق")
    reason_details = f"باص: {bus}, زحمة: {traffic}"
elif target == "غبت عن محاضرة":
    with col1: sick = st.checkbox("عندي سكليف")
    with col2: family = st.checkbox("ظرف عائلي")
    reason_details = f"مرض: {sick}, عائلي: {family}"
elif target == "تنزيل مادة أو فتح شعبة":
    with col1: nafaz = st.checkbox("نفاذ معلق")
    with col2: grad = st.checkbox("خريج/ة")
    reason_details = f"نفاذ: {nafaz}, تخرج: {grad}"
elif target == "تغيير شعبة":
    with col1: conflict = st.checkbox("تعارض مواد")
    with col2: qaila = st.checkbox("وقت القايلة (حر)")
    reason_details = f"تعارض: {conflict}, قايلة: {qaila}"
elif target == "طلب إعفاء لغة إنجليزية":
    with col1: sent_request = st.checkbox("قدمت طلب سابقاً ولم يحذف المقرر")
    with col2: urgency = st.checkbox("باشروا في طلبي (عاجل)")
    reason_details = f"قدمت طلب ولم يحذف: {sent_request}, استعجال: {urgency}"

st.markdown('</div>', unsafe_allow_html=True)

mood = st.select_slider("🎭 أسلوب الرسالة:", options=["رسمي جداً", "نظامي", "حبيب/ة"], value="نظامي")

# 6. التشغيل
if st.button("🚀 ولّد الإيميل الفزعة"):
    with st.spinner('جاري حبك الأعذار...'):
        try:
            if target == "طلب إعفاء لغة إنجليزية":
                prompt = f"اكتب رسالة موجهة لعمادة القبول والتسجيل بخصوص {target}. التفاصيل: {reason_details}. أسلوب الرسالة: {mood}. اطلب منهم مباشرة إجراءات الإعفاء وحذف المقرر لأن الطلب مقدم مسبقاً ولم يتم الحذف. بلهجة بيضاء محترمة."
            else:
                prompt = f"اكتب إيميل لـ {target}. التفاصيل: {reason_details}. أسلوب المتلقي: {mood}. بلهجة بيضاء محترمة."
            
            res = model.generate_content(prompt)
            st.session_state['generated_email'] = res.text
        except Exception as e:
            st.error(f"حدث خطأ: {e}")

if 'generated_email' in st.session_state:
    st.markdown("---")
    st.subheader("📬 إيميلك الجاهز:")
    st.info(st.session_state['generated_email'])
    
    st.download_button(label="📥 تحميل الإيميل (نص)", data=st.session_state['generated_email'], file_name="fazaa_email.txt", mime="text/plain")
    
    st.markdown("---")
    if st.button("🧐 اسأل 'المُدقق الفزعة' عن نسبة القبول"):
        with st.spinner('المُدقق يراجع إيميلك بذكاء...'):
            check_p = f"حلل هذا الإيميل: '{st.session_state['generated_email']}'. أعطني نسبة قبول العمادة لهذا الطلب من 100، واكتب نصيحة قصيمية سريعة جداً لصاحب الإيميل."
            analysis = model.generate_content(check_p)
            st.success(analysis.text)
            st.balloons()

st.markdown(f'<div style="text-align:center; color:#888; margin-top:50px;">تطوير المهندسة حنين 1/2 | GDG Qassim 🚀</div>', unsafe_allow_html=True)
