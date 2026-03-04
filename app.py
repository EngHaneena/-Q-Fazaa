import streamlit as st
import google.generativeai as genai
import random

# 1. إعدادات الصفحة والهوية البصرية
st.set_page_config(page_title="Q-Fazaa | كيو فزعة", page_icon="🎓", layout="centered")

# CSS المتقدم (ثابت ومستقر)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; text-align: right; direction: rtl; }
    .main-header { background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%); color: white; padding: 30px; border-radius: 20px; text-align: center; margin-bottom: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
    .main-header h1 { color: white !important; margin: 0; }
    .main-header p { color: #f8f9fa !important; margin: 5px 0 0; font-size: 1.1em; }
    .joke-box { background-color: #fff9db; color: #856404; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 25px; font-weight: bold; border: 2px dashed #fcc419; font-size: 18px; }
    .option-card { background-color: white; padding: 20px; border-radius: 15px; border-right: 8px solid #1a73e8; box-shadow: 0 2px 8px rgba(0,0,0,0.05); margin-bottom: 20px; color: #333; }
    .stButton>button { background: linear-gradient(45deg, #1a73e8, #0d47a1); color: white; height: 3em; border-radius: 12px; font-size: 18px !important; transition: 0.3s; border: none; font-weight: bold; width: 100%; }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 5px 15px rgba(26,115,232,0.4); }
    /* تنسيق نتيجة المُدقق (HTML) */
    .analysis-box { background-color: #e3f2fd; color: #0d47a1; padding: 20px; border-radius: 15px; border: 1px solid #90caf9; margin-top: 20px; text-align: right; }
    .analysis-box h3 { color: #0d47a1 !important; margin-top: 0; }
    .analysis-box p { margin: 8px 0; }
    @media (prefers-color-scheme: dark) {
        .option-card { background-color: #1a1a1a !important; color: #f8f9fa !important; border-right: 8px solid #4dadff !important; }
        .joke-box { background-color: #2b2b2b !important; color: #ffd43b !important; border-color: #fab005 !important; }
        .analysis-box { background-color: #1a1a1a !important; color: #4dadff !important; border-color: #0d47a1 !important; }
        .analysis-box h3 { color: #4dadff !important; }
        h1, h2, h3, h4, p, span, label { color: white !important; }
    }
    </style>
    """, unsafe_allow_html=True)

# 2. إعداد الـ API (ثابت ومستقر)
try:
    api_key = st.secrets.get("GOOGLE_API_KEY")
    genai.configure(api_key=api_key)
    # استخدام موديل Gemini 1.5 Flash للسرعة والدقة
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    st.error(f"⚠️ تأكدي من إعداد الـ API Key في الـ Secrets. الخطأ: {e}")
    st.stop()

# 3. الهيدر (تم تحديث الشعار)
st.markdown('<div class="main-header"><h1>🎓 كيو فزعة | Q-Fazaa</h1><p>فزعتك بيدك.. وإيميلك بثواني يجيك ⚡</p></div>', unsafe_allow_html=True)

# 4. الأهداف (ثابت ومستقر)
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

# قاموس الذبات (تم تحديث ذبة الإعفاء)
# قاموس الذبات (تم تحديث ذبة تأخر الباص)
jokes = {
    "طلب بونص درجات": ["تكفى يا دكتوور.. بمسك عيالك بس عطني هالعشر درجات هههههه"],
    "تحويل المحاضرة أونلاين": ["طريق المليداء اليوم يبي له طيارة مب سيارة.. خلوها عن بعد!"],
    "تأخر عن محاضرة": ["باص الجامعة سحب علي!! تراها قاافلة! "],
    "غبت عن محاضرة": ["السكليف جاهز.. بس الحالة ماش "],
    "تنزيل مادة أو فتح شعبة": ["نفاذ معلق.. وبوابة الجامعة مو راضية تبطللل! "],
    "تغيير شعبة": ["الوقت بعز القايلة يا دكتور.. والأخلاق وسط "],
    "طلب إعفاء لغة إنجليزية": ["بيحذفونه لك معليك بلا تهاويل!هههههههه"]
}

if target in jokes:
    st.markdown(f'<div class="joke-box">💡 {random.choice(jokes[target])}</div>', unsafe_allow_html=True)

# 5. منطقة التفاصيل (ثابت ومستقر)
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

# 6. التشغيل (تم تحديث البرومبتات لبرومبتات احترافية وهيكلية)
if st.button("🚀 ولّد الإيميل الفزعة"):
    with st.spinner('جاري حبك الأعذار باحترافية...'):
        try:
            # 🌟 برومبت "إيجنت الكاتب" الاحترافي الجديد
            if target == "طلب إعفاء لغة إنجليزية":
                # برومبت مخصص لعمادة القبول والتسجيل
                prompt = f"""
أنت الآن تعمل كـ "مساعد أكاديمي ذكي" متخصص في صياغة الرسائل الرسمية لطلاب جامعة القصيم الموجهة لعمادة القبول والتسجيل.

[السياق والهدف]:
الهدف هو كتابة رسالة موجهة لعمادة القبول والتسجيل بخصوص طلب "{target}". التفاصيل: {reason_details}. اطلب منهم مباشرة إجراءات الإعفاء وحذف المقرر لأن الطلب مقدم مسبقاً ولم يتم الحذف.

[القيود والتعليمات]:
1. **النبرة والأسلوب:** يجب أن تكون النبرة مناسبة جداً لأسلوب الرسالة المحدد: "{mood}".
   - إذا كان "رسمي جداً": استخدم مصطلحات أكاديمية رفيعة، وتجنب أي طابع ودي.
   - إذا كان "نظامي": التزم باللوائح والأنظمة بوضوح واحترام.
   - إذا كان "حبيب/ة": استخدم أسلوباً مهذباً ولطيفاً يعبر عن التقدير العالي للعمادة.
2. **اللغة:** استخدم لغة عربية بيضاء مهذبة، سليمة قواعدياً، وابتعد عن العامية المبتذلة، مع الحفاظ على الهوية المحلية المحترمة.
3. **الاختصار:** اجعل الرسالة مركزة ومباشرة دون إسهاب ممل، مع توضيح العذر وطلب الطالب بوضوح.
4. **بنية الرسالة:** يجب أن تتكون الرسالة من:
   - تحية رسمية مناسبة للعمادة.
   - جملة افتتاحية مهذبة.
   - صياغة احترافية لطلب الإعفاء واستعجال الحذف.
   - جملة ختامية تعبر عن الشكر والتقدير.
   - التوقيع (مكان لاسم الطالب والرقم الجامعي).

[النتيجة المتوقعة]:
نص الرسالة الجاهز للإرسال فقط، دون أي مقدمات أو شروحات إضافية منك.
                """
            else:
                # برومبت مخصص للدكتور
                prompt = f"""
أنت الآن تعمل كـ "مساعد أكاديمي ذكي" متخصص في صياغة الرسائل الرسمية لطلاب جامعة القصيم الموجهة للدكاترة.

[السياق والهدف]:
الهدف هو كتابة رسالة إيميل احترافية ومقنعة موجهة إلى "{target}" بناءً على تفاصيل العذر التالية: {reason_details}.

[القيود والتعليمات]:
1. **النبرة والأسلوب:** يجب أن تكون النبرة مناسبة جداً لأسلوب المتلقي المحدد: "{mood}".
   - إذا كان "رسمي جداً": استخدم مصطلحات أكاديمية رفيعة، وتجنب أي طابع ودي.
   - إذا كان "نظامي": التزم باللوائح والأنظمة بوضوح واحترام.
   - إذا كان "حبيب/ة": استخدم أسلوباً مهذباً ولطيفاً يعبر عن التقدير العالي للدكتور/ة.
2. **اللغة:** استخدم لغة عربية بيضاء مهذبة، سليمة قواعدياً، وابتعد عن العامية المبتذلة، مع الحفاظ على الهوية المحلية المحترمة.
3. **الاختصار:** اجعل الرسالة مركزة ومباشرة دون إسهاب ممل، مع توضيح العذر وطلب الطالب بوضوح.
4. **بنية الرسالة:** يجب أن تتكون الرسالة من:
   - تحية رسمية مناسبة للمتلقي والمود.
   - جملة افتتاحية مهذبة.
   - صياغة احترافية للعذر وطلب الطالب (تخفيض درجات، تأخير، غياب، تغيير شعبة).
   - جملة ختامية تعبر عن الشكر والتقدير.
   - التوقيع (مكان لاسم الطالب والرقم الجامعي).

[النتيجة المتوقعة]:
نص الإيميل الجاهز للإرسال فقط، دون أي مقدمات أو شروحات إضافية منك.
                """
            
            res = model.generate_content(prompt)
            # تخزين الإيميل المولد في الـ Session State
            st.session_state['generated_email'] = res.text
        except Exception as e:
            st.error(f"حدث خطأ في توليد الإيميل: {e}")

# عرض الإيميل المُولد (ثابت ومستقر)
if 'generated_email' in st.session_state:
    st.markdown("---")
    st.subheader("📬 إيميلك الجاهز:")
    st.info(st.session_state['generated_email'])
    
    # زر التحميل (ثابت ومستقر)
    st.download_button(label="📥 تحميل الإيميل (نص)", data=st.session_state['generated_email'], file_name="fazaa_email.txt", mime="text/plain")
    
    st.markdown("---")
    # 7. المُدقق الفزعة (تم تحديث البرومبت لبرومبت تحليلي واحترافي)
    if st.button("🧐 اسأل 'المُدقق الفزعة' عن نسبة القبول"):
        with st.spinner('المُدقق يراجع إيميلك باحترافية قصيمية...'):
            try:
                # 🌟 برومبت "إيجنت المُدقق" الاحترافي الجديد (التحليلي)
                check_p = f"""
أنت الآن "خبير تحليل خطابات أكاديمية وفزعة قصيمية". وظيفتك هي مراجعة الإيميل التالي الذي كتبه طالب لـ "{target}" بناءً على عذر "{reason_details}"، وتقديم تقييم شامل.

[الإيميل المراد تحليله]:
"{st.session_state['generated_email']}"

[التعليمات والمهام]:
1. **تحليل القبول:** حلل لغة الإيميل، قوة العذر، ومدى لباقته. بناءً على هذا التحليل، قدم نسبة مئوية متوقعة لقبول الدكتور أو العمادة لهذا الطلب (من 100%).
2. **اللمسة الفزعة (الفيدباك):** قدم نصيحة قصيمية سريعة جداً، ودية، ومطمئنة لصاحب الإيميل. يجب أن تعبر النكتة عن روح الفزعة القصيمية المعهودة (مثال: 'بيحذفونه لك بلا تهاويل!').
3. **ملاحظات تحسين (اختياري):** إذا كانت نسبة القبول أقل من 70%، اذكر باختصار شديد نقطة واحدة يمكن تحسينها في الإيميل (مثال: 'النبرة محتاجة تكون أكثر رسمية').

[النتيجة المتوقعة]:
أخرج النتيجة بتنسيق HTML واضح:
<div class="analysis-box">
  <h3>📊 تقييم المُدقق الفزعة</h3>
  <p><b>نسبة القبول المتوقعة:</b> [النسبة]%</p>
  <p><b>💡 نصيحة الفزعة:</b> [النصيحة القصيمية الودية والفكاهية]</p>
  [إذا كانت النسبة منخفضة: <p><b>🔧 تحسين مقترح:</b> [الملاحظة المختصرة]</p>]
</div>
"""
                analysis = model.generate_content(check_p)
                # عرض نتيجة التحليل (التي تأتي بتنسيق HTML من البرومبت)
                st.markdown(analysis.text, unsafe_allow_html=True)
                st.balloons()
            except Exception as e:
                st.error(f"حدث خطأ في المُدقق: {e}")

# الفوتر (تم تحديث التوقيع)
st.markdown(f'<div style="text-align:center; color:#888; margin-top:50px; font-family: \'Courier New\', Courier, monospace;"> GDG Qassim 🚀 - By Eng Haneen</div>', unsafe_allow_html=True)


