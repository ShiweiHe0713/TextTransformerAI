# TextTransformerAI
Automate text processing and OpenAI API interactions in Python. Transform text files into valuable insights, perfect for developers and content creators. Streamline data cleaning, content generation, and insight extraction with ease

## Purpose Cleared
We have a raw txt file consists of roughly 8500 figures from previous dynasty, but the txt is only seperated by "【", "】", and new line. We want to extract their name, position, tribute, hometown, etc and store all the information into a `xlsx` file with those columns.

## Steps
1. Turn `txt` file into an array of string
![txt to array](assets/images/image.png)

2. Feed the array into LLM
Now we are picking GPT-turbo-3.5 as our model. So we will take the array we have from last step to GPT, and get the target output that we want.
- Raw data entry: "明田载【北平人永乐中知铜仁府时初立郡载结庐听政招集遗氓踰年官署学宫规制渐备外 驯蛮獠内抚疮痍民赖以安】"
- Output format: '人物姓名', '最高官职', '功名', '籍贯（哪里人）', '所处朝代', '入志缘由', '入志原因', '其他'
- Target output: 明田载, 知府, NA, 北平人, 明朝，抚疮痍民，5 (Could be wrapped in quotes "")

3. Further process the output from step 2
We will have roughly 8500 entries of the data like "明田载, 知府, NA, 北平人, 明朝，抚疮痍民，5", we store them either in:
- An array of 8500 rows * 1 column
  - Then traverse the array and insert them into `xlsx` file, each column is seperated by comma in the entry
- A `csv` file with 8500 rows ✅
  - Turn the array into csv, it's easier this way, since we can first turn the array into a dataframe, and directly use `to_excel` to a `xlsx` file.

