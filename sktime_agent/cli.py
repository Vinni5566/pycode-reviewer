import click
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from .core import generate_dummy_response

console = Console()

@click.command()
@click.argument('query')
@click.option('--agent', is_flag=True, help="Use real LLM agent instead of dummy response")
def main(query: str, agent: bool):
    """
    Agentic sktime Assistant - Conversational Workflow Generator
    """
    console.print(f"[bold blue]Query:[/bold blue] {query}\n")
    
    with console.status("[bold green]Generating sktime workflow..."):
        from .core import generate_response
        response = generate_response(query, use_agent=agent)
    
    console.print(Panel(response.explanation, title="Explanation", expand=False))
    
    console.print("\n[bold]Generated sktime Code:[/bold]")
    syntax = Syntax(response.code, "python", theme="monokai", line_numbers=True)
    console.print(syntax)
    
    if response.evaluation:
        console.print("\n[bold]Optional Evaluation Snippet:[/bold]")
        eval_syntax = Syntax(response.evaluation, "python", theme="monokai", line_numbers=True)
        console.print(eval_syntax)

if __name__ == "__main__":
    main()
