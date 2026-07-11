%global tl_name opcit
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Footnote-style bibliographical references
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/opcit
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/opcit.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/opcit.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/opcit.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package addresses the problem of expressing citations in a style
that is natural for humanities studies, yet does not interfere with the
flow of text (as author-year styles do). The package differs from
footbib in that it uses real footnotes, potentially in the same series
as any of the document's other footnotes. Opcit also, as its name
implies, avoids repetition of full citations, achieving this, to a large
extent, automatically.

