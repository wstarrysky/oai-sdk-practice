from openai_codex import Codex, Sandbox

with Codex() as codex:
    thread = codex.thread_start(
        model="gpt-5.6-terra",
        sandbox=Sandbox.workspace_write,
        cwd="E:\\VBC\\oai-sdk-practice",
    )
    # 先用最小问答验证 SDK 链路和返回值
    result = thread.run("请只回复：SDK 调用成功")
    print(result.final_response)
