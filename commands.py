from database import add_task, delete_task, show_tasks, complete_task

async def add_task_command(ctx, description):
    add_task(description)
    await ctx.send(f'Task added: {description}')

async def delete_task_command(ctx, task_id):
    delete_task(task_id)
    await ctx.send(f'Task deleted: {task_id}')

async def show_tasks_command(ctx):
    tasks = show_tasks()
    if not tasks:
        await ctx.send('No tasks available.')
    else:
        task_list = '\n'.join([f'{task[0]}: {"[✓]" if task[2] else "[ ]"} {task[1]}' for task in tasks])
        await ctx.send(f'Tasks:\n{task_list}')

async def complete_task_command(ctx, task_id):
    complete_task(task_id)
    await ctx.send(f'Task marked as complete: {task_id}')
