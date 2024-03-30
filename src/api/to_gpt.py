import openai

def toGPT(text_arr):
    prompt = """
            请帮我提取以下信息：1、姓名（【之前的内容均为姓名）2、官职（取最大官职，保留一个） 3、功名（看是否是进士，如果不是则标记为NA） 4、籍贯（可调用GPT自己的知识库提供） 
            5、生活朝代（可调用GPT自己的知识库提供，格式为xxx朝） 6、入志缘由（请根据行内容进行五个字以内概述）7、入志原因（只需要根据所提供语料保留1个数字序号就好，
            具体标准为：1=忠臣；2=良将；3=廉吏；4=政绩；5=儒学；6=书法艺术；7=孝道；8=其他）.
            提取出的信息请以逗号来分隔，返回内容里不能包含栏目名称（比如“功名”）
            """
    processed_text = []
    chunk_size = 15 # Process 15 people at a time

    for start in range(0, len(text_arr), chunk_size):
        end = start + chunk_size
        text_chunk = text_arr[start:end]        
        

    # making api calls
