from autogen_agentchat.agents import CodeExecutorAgent
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from autogen_core


async def main():
    
    docker = DockerCommandLineCodeExecutor(
        work_dir = "/tmp",
        timeout = 120
    )
    
    code_executor_agent = CodeExecutorAgent(
        name = "CodeExecutorAgent",
        code_executor = docker
    )
    
    
    task = TextMessage(
        content = '''Here is some code
        ```python
        print('Hello world')
        ```
        ''',
        source = "user"
        
        await docker.start()
        
        
    )
    
    response = await code_executor_agent.on_messages([task], CancellationToken())
    
    print(response.chat_message)


if __name__ == "__main__":
    asyncio.run(main())