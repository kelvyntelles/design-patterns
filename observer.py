from abc import ABC, abstractmethod


class IObserverNoticia(ABC):
    @abstractmethod
    def noticia_criada(self, titulo: str, cidade: str) -> None:
        pass


class IObservable(ABC):
    @abstractmethod
    def add_observer(self, observer: IObserverNoticia) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserverNoticia) -> None:
        pass

    @abstractmethod
    def notify_observers(self, titulo: str, cidade: str) -> None:
        pass


class Leitor(IObserverNoticia):
    def __init__(self, nome: str):
        self.nome = nome

    def noticia_criada(self, titulo: str, cidade: str) -> None:
        print(
            f"[{self.nome}] Nova notícia em {cidade}: {titulo}!"
        )


class Jornal(IObservable):
    def __init__(self):
        self.observers: list[IObserverNoticia] = []

    def add_observer(self, observer: IObserverNoticia) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer: IObserverNoticia) -> None:
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, titulo: str, cidade: str) -> None:
        for observer in self.observers:
            observer.noticia_criada(titulo, cidade)

    def criar_noticia(self, titulo: str, cidade: str) -> None:
        print(f"\n[Jornal] Notícia criada em {cidade}: {titulo}")

        self.notify_observers(titulo, cidade)


# Subject / Observable
jornal = Jornal()


# Observers
leitor1 = Leitor("Leitor 1")
leitor2 = Leitor("Leitor 2")
leitor3 = Leitor("Leitor 3")


# Inscrevendo os leitores
jornal.add_observer(leitor1)
jornal.add_observer(leitor2)
jornal.add_observer(leitor3)


# Criando uma notícia
jornal.criar_noticia(
    "Festival de Música acontece neste sábado",
    "Vassouras"
)


# Removendo um observer
jornal.remove_observer(leitor2)


# Criando outra notícia
jornal.criar_noticia(
    "Novo restaurante é inaugurado no centro",
    "Vassouras"
)