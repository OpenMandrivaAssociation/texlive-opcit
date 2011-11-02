Name:		texlive-opcit
Version:	1.1
Release:	1
Summary:	Footnote-style bibliographical references
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/opcit
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/opcit.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/opcit.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/opcit.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package addresses the problem of expressing citations in a
style that is natural for humanities studies, yet does not
interfere with the flow of text (as author-year styles do). The
package differs from footbib in that it uses real footnotes,
potentially in the same series as any of the document's other
footnotes. Opcit also, as its name implies, avoids repetition
of full citations, achieving this, to a large extent,
automatically.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/opcit/opcit.bst
%{_texmfdistdir}/tex/latex/opcit/opcit.sty
%doc %{_texmfdistdir}/doc/latex/opcit/README
%doc %{_texmfdistdir}/doc/latex/opcit/opcit.pdf
#- source
%doc %{_texmfdistdir}/source/latex/opcit/opcit.dtx
%doc %{_texmfdistdir}/source/latex/opcit/opcit.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
